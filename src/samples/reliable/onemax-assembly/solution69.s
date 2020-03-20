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

    movl	$-18812, %eax
    movl	$10538, %ebx
    movl	$30285, %ecx
    movl	$21227, %edx

    cmp %edx, %ecx
    jno n24
    shl $30, %ebx
    jc n21
    shr $123, %ebx
    shl $222, %edx
    jc n12
    je n24
    shl $146, %ebx
n12:
    and %ebx, %edx
    shr $58, %ebx
    shr $14, %ebx
    shl $237, %edx
    jno n23
    jnc n18
n18:
    shr $81, %ecx
    jnz n20
n20:
    jne n23
n21:
    cmp %ebx, %eax
    cmp %edx, %eax
n23:
    ja n24
n24:
    jc n26
    jz n26
n26:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
