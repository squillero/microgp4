    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-11084, %eax
    movl	$2792, %ebx
    movl	$-2234, %ecx
    movl	$-5520, %edx

    shr $105, %edx
    shl $10, %edx
    shl $3, %ecx
    and %edx, %edx
    xor %ebx, %edx
    shr $139, %edx
    shl $14, %edx
    shl $207, %ebx
    or %ebx, %eax
    shl $13, %eax
    cmp %edx, %ebx
    jo n26
    shr $133, %edx
    and %ebx, %edx
    and %ecx, %edx
    and %edx, %ecx
    jz n35
    shr $26, %ecx
    sub %eax, %eax
    shr $126, %ebx
    add %ebx, %ebx
    shr $242, %eax
    jmp n32
n26:
    or %ecx, %ecx
    sub %eax, %ebx
    jne n32
    shr $159, %edx
    or %ebx, %eax
    jmp n43
n32:
    cmp %ebx, %eax
    cmp %ecx, %eax
    xor %eax, %ecx
n35:
    shl $189, %eax
    jno n42
    ja n44
    jo n40
    jnc n42
n40:
    cmp %edx, %ebx
    shl $90, %ecx
n42:
    jmp n46
n43:
    shl $223, %ecx
n44:
    jc n45
n45:
    jz n46
n46:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
