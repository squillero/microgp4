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

    movl	$16366, %eax
    movl	$22119, %ebx
    movl	$-32281, %ecx
    movl	$30774, %edx

    shl $237, %eax
    jnz n11
    jmp n22
    jno n31
    add %ebx, %edx
    or %ecx, %eax
    shr $162, %ebx
    and %edx, %ecx
n11:
    add %eax, %eax
    and %ebx, %ecx
    jnc n18
    and %ecx, %edx
    jz n32
    and %eax, %edx
    shl $153, %edx
n18:
    add %eax, %ecx
    shl $94, %eax
    shr $51, %ecx
    shr $48, %ecx
n22:
    and %ecx, %eax
    shr $108, %eax
    je n25
n25:
    jne n30
    jno n35
    shr $152, %ecx
    jz n35
    ja n32
n30:
    or %eax, %ecx
n31:
    shl $26, %ebx
n32:
    jz n33
n33:
    xor %eax, %eax
    shl $21, %edx
n35:
    and %edx, %eax
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
